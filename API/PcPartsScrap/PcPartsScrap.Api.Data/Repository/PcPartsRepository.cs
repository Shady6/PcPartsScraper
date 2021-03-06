using Microsoft.EntityFrameworkCore;
using PcPartsScrap.Api.Data.Entities;
using PcPartsScrap.Api.Data.Repository.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Api.Data.Repository
{
	public class PcPartsRepository : IPcPartsRepository
	{
		protected readonly PcPartsDbContext _dbContext;

		public PcPartsRepository(PcPartsDbContext dbContext)
		{
			_dbContext = dbContext;
		}

		// TODO clean clode here, instead of multiple arguments change to one filter
		// add automapper to not return id from db
		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTimeAndPrice(
			string category,
			string[] producentCodes,
			DateTime? minListingDate = null,
			DateTime? maxListingDate = null,
			int? minPrice = null,
			int? maxPrice = null
			)
		{
			return
				GetItemsInCategoryWithinPrice(category, producentCodes, minPrice, maxPrice, maxListingDate,
				GetItemsInCategoryWithinTime(category, producentCodes, minListingDate, maxListingDate));
		}

		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTime(
			string category,
			string[] producentCodes,
			DateTime? minListingDate = null,
			DateTime? maxListingDate = null,
			IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null
			)
		{
			var result = itemsInCategory ?? GetItemsInCategory(category, producentCodes);

			if (minListingDate == null && maxListingDate == null)
				return result;
			else if (minListingDate == null)
				result
				   .Select(g => new Grouping<string, PCParts>
				   {
					   Key = g.Key,
					   Elements = g.Where(p => p.ListingDate <= maxListingDate)
				   });
			else
				result
				   .Select(g => new Grouping<string, PCParts>
				   {
					   Key = g.Key,
					   Elements = g.Where(p => p.ListingDate >= minListingDate && p.ListingDate <= maxListingDate)
				   });

			return OrderGroupByDateDesc(result);
		}

		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinPrice(
			string category,
			string[] producentCodes,
			int? minPrice = null,
			int? maxPrice = null,
			DateTime? tillDate = null,
			IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null
			)
		{
			var result = itemsInCategory ?? GetItemsInCategory(category, producentCodes);
			tillDate = tillDate ?? DateTime.Now;

			if (minPrice == null && maxPrice == null)
				return result;
			else if (minPrice == null)
				result
				   .Select(g => new Grouping<string, PCParts>
				   {
					   Key = g.Key,
					   Elements = GetLatestPriceTillDate(g, (DateTime)tillDate) <= maxPrice ? g : new List<PCParts>()
				   });
			else
				result
					.Select(g =>
					{
						int latestPriceInGroup = GetLatestPriceTillDate(g, (DateTime)tillDate);
						return new Grouping<string, PCParts>
						{
							Key = g.Key,
							Elements = latestPriceInGroup >= minPrice && latestPriceInGroup <= maxPrice ? g : new List<PCParts>()
						};
					});

			return OrderGroupByDateDesc(result);
		}

		private IEnumerable<IGrouping<string, PCParts>> OrderGroupByDateDesc(IEnumerable<IGrouping<string, PCParts>> result)
		{
			return result.SelectMany(g => g).OrderByDescending(p => p.ListingDate).GroupBy(p => p.ProducentCode);
		}		

		private int GetLatestPriceTillDate(IGrouping<string, PCParts> group, DateTime date)
		{
			PCParts latestPart = group.Where(p => p.ListingDate == group.Max(
				pcp => pcp.ListingDate <= date ? pcp.ListingDate : DateTime.MinValue))
				.FirstOrDefault();

			return latestPart == null ? 0 : latestPart.Price;
		}

		public IEnumerable<string> GetCategories() =>
			 _dbContext.PcParts
				.Select(p => p.Category)
				.Distinct()
				.AsNoTracking();

		public Dictionary<string, string> GetItemsNamesInCategory(string category) =>
			_dbContext.PcParts.Where(p => p.Category == category)
			.AsEnumerable()
			.GroupBy(p => p.ProducentCode)
			.ToDictionary(g => g.Key, g => g.First().DetailedName)
			.AsEnumerable()
			.OrderBy(d => d.Value)
			.ToDictionary(o => o.Key, o => o.Value);

		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategory(string category, string[] producentCodes) =>
			_dbContext.PcParts.Where(p => p.Category == category && producentCodes.Contains(p.ProducentCode))
			.AsEnumerable()
			.GroupBy(p => p.ProducentCode);
	}
}
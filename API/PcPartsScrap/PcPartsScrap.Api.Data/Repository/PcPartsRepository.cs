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
		
		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTimeAndPrice(
			string category,
			SearchFilter filter
			)
		{
			return
				GetItemsInCategoryWithinPrice(category, filter, filter.MaxListingDate,
				GetItemsInCategoryWithinTime(category, filter));
		}

		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTime(
			string category,
			SearchFilter filter,
			IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null
			)
		{
			var result = itemsInCategory ?? GetItemsInCategory(category, filter.ProducentCodes);

			if (filter.MinListingDate == null && filter.MaxListingDate == null)
				return result;
			else if (filter.MinListingDate == null)
				result = result
				   .Select(g => new Grouping<string, PCParts>
				   {
					   Key = g.Key,
					   Elements = g.Where(p => p.ListingDate <= filter.MaxListingDate)
				   });
			else
				result = result
				   .Select(g => new Grouping<string, PCParts>
				   {
					   Key = g.Key,
					   Elements = g.Where(p => p.ListingDate >= filter.MinListingDate && p.ListingDate <= filter.MaxListingDate)
				   });

			return OrderGroupByDateDesc(result);
		}

		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinPrice(
			string category,
			SearchFilter filter,
			DateTime? tillDate = null,
			IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null
			)
		{
			var result = itemsInCategory ?? GetItemsInCategory(category, filter.ProducentCodes);
			tillDate ??= DateTime.Now;

			if (filter.MinPrice == null && filter.MaxPrice == null)
				return result;
			else if (filter.MinPrice == null)
				result = result
				   .Select(g => new Grouping<string, PCParts>
				   {
					   Key = g.Key,
					   Elements = GetLatestPriceTillDate(g, (DateTime)tillDate) <= filter.MaxPrice ? g : new List<PCParts>()
				   });
			else
				result = result
					.Select(g =>
					{
						int latestPriceInGroup = GetLatestPriceTillDate(g, (DateTime)tillDate);
						return new Grouping<string, PCParts>
						{
							Key = g.Key,
							Elements = latestPriceInGroup >= filter.MinPrice && latestPriceInGroup <= filter.MaxPrice ? g : new List<PCParts>()
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
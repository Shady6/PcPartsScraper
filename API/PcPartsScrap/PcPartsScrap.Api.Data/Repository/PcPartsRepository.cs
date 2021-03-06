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
			string[] producentCodes,
			DateTime? minListingDate = null,
			DateTime? maxListingDate = null,
			int? minPrice = null,
			int? maxPrice = null
			)
		{
			return
				GetItemsInCategoryWithinCurrentPrice(category, producentCodes, minPrice, maxPrice,
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
				return result.SelectMany(g => g)
					.Where(p => p.ListingDate <= maxListingDate)
					.AsEnumerable()
					.GroupBy(p => p.ProducentCode);
			else
				return result.SelectMany(g => g)
					.Where(p => p.ListingDate >= minListingDate && p.ListingDate <= maxListingDate)
					.AsEnumerable()
					.GroupBy(p => p.ProducentCode);
		}

		public IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinCurrentPrice(
			string category,
			string[] producentCodes,
			int? minPrice = null,
			int? maxPrice = null,
			IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null
			)
		{
			Func<IGrouping<string, PCParts>, int> GetLatestPrice = g => g.Where(p => p.ListingDate == g.Max(pcp => pcp.ListingDate)).First().Price;
			var result = itemsInCategory ?? GetItemsInCategory(category, producentCodes);

			if (minPrice == null && maxPrice == null)
				return result;
			else if (minPrice == null)
				return result.Where(g => GetLatestPrice(g) <= maxPrice);
			else
				return result.Where(g => GetLatestPrice(g) >= minPrice && GetLatestPrice(g) <= maxPrice);
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
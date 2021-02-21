using PcPartsScrap.Wcf.Data.Entities;
using PcPartsScrap.Wcf.Data.Repository.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Wcf.Data.Repository
{
	public class PcPartsRepository : IPcPartsRepository
	{
		protected readonly PcPartsDbContext _dbContext;

		public PcPartsRepository(PcPartsDbContext dbContext)
		{
			_dbContext = dbContext;
		}

		public IEnumerable<IGrouping<string, PcPart>> GetItemsInCategoryWithinTimeAndPrice(
			string category,
			List<string> producentCodes,
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

		public IEnumerable<IGrouping<string, PcPart>> GetItemsInCategoryWithinTime(
			string category,
			List<string> producentCodes,
			DateTime? minListingDate = null,
			DateTime? maxListingDate = null,
			IEnumerable<IGrouping<string, PcPart>> itemsInCategory = null
			)
		{
			var result = itemsInCategory ?? GetItemsInCategory(category, producentCodes);

			if (minListingDate == null && maxListingDate == null)
				return result;
			else if (minListingDate == null)
				return result.SelectMany(g => g)
					.Where(p => p.ListingDate <= maxListingDate)
					.GroupBy(p => p.ProducentCode);
			else
				return result.SelectMany(g => g)
					.Where(p => p.ListingDate >= minListingDate && p.ListingDate <= maxListingDate)
					.GroupBy(p => p.ProducentCode);
		}

		public IEnumerable<IGrouping<string, PcPart>> GetItemsInCategoryWithinCurrentPrice(
			string category,
			List<string> producentCodes,
			int? minPrice = null,
			int? maxPrice = null,
			IEnumerable<IGrouping<string, PcPart>> itemsInCategory = null
			)
		{
			Func<IGrouping<string, PcPart>, int> GetLatestPrice = g => g.Where(p => p.ListingDate == g.Max(pcp => pcp.ListingDate)).First().Price;
			var result = itemsInCategory ?? GetItemsInCategory(category, producentCodes);

			if (minPrice == null && maxPrice == null)
				return result;
			else if (minPrice == null)
				return result.Where(g => GetLatestPrice(g) <= maxPrice);
			else
				return result.Where(g => GetLatestPrice(g) >= minPrice && GetLatestPrice(g) <= maxPrice);
		}

		public IEnumerable<string> GetCategories() =>
			_dbContext.PcParts.GroupBy(p => p.Category)
				.Select(g => g.Key)
				.OrderBy(g => g);

		public Dictionary<string, string> GeItemsNamesInCategory(string category) =>
			_dbContext.PcParts.Where(p => p.Category == category)
			.GroupBy(p => p.ProducentCode)
			.ToDictionary(g => g.Key, g => g.First().DetailedName)
			.OrderBy(d => d.Value)
			.ToDictionary(o => o.Key, o => o.Value);

		public IEnumerable<IGrouping<string, PcPart>> GetItemsInCategory(string category, List<string> producentCodes) =>
			_dbContext.PcParts.Where(p => p.Category == category && producentCodes.Contains(p.ProducentCode))
			.GroupBy(p => p.ProducentCode)
			.OrderBy(g => g.First());
	}
}
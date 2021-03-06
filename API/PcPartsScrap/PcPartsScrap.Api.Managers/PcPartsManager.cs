using PcPartsScrap.Api.Common.Extensions;
using PcPartsScrap.Api.Data;
using PcPartsScrap.Api.Data.Entities;
using PcPartsScrap.Api.Data.Repository.Interfaces;
using PcPartsScrap.Api.Managers.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Api.Managers
{
	public class PcPartsManager : IPcPartsManager
	{
		private readonly IPcPartsRepository _pcPartsRepo;

		public PcPartsManager(IPcPartsRepository pcPartsRepo)
		{
			_pcPartsRepo = pcPartsRepo;			
		}

		public Dictionary<string, List<PCParts>> SearchItemsWithFilter(string category, SearchFilter filter)
		{
			switch (filter.filterBy.ToEnum<FilterBy>())
			{
				case FilterBy.Price:
					return GetItemsInCategoryWithinCurrentPrice(category, filter.producentCodes, filter.minPrice, filter.maxPrice);

				case FilterBy.Date:
					return GetItemsInCategoryWithinTime(category, filter.producentCodes, filter.minListingDate, filter.maxListingDate);

				case FilterBy.PriceAndDate:
					return GetItemsInCategoryWithinTimeAndPrice(category, filter.producentCodes, filter.minListingDate, filter.maxListingDate, filter.minPrice, filter.maxPrice);

				default:
					return GetItemsInCategory(category, filter.producentCodes);
			}
		}

		public string[] GetCategories()
		{
			return _pcPartsRepo.GetCategories().ToArray();
		}

		public Dictionary<string, string> GetItemsNamesInCategory(string category)
		{
			return _pcPartsRepo.GetItemsNamesInCategory(category);
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategoryWithinTimeAndPrice(
			string category,
			string[] producentCodes,
			DateTime? minListingDate = null,
			DateTime? maxListingDate = null,
			int? minPrice = null,
			int? maxPrice = null
			)
		{
			return _pcPartsRepo.GetItemsInCategoryWithinTimeAndPrice(category, producentCodes, minListingDate, maxListingDate, minPrice, maxPrice)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategoryWithinTime(
			string category,
			string[] producentCodes,
			DateTime? minListingDate = null,
			DateTime? maxListingDate = null
			)
		{
			return _pcPartsRepo.GetItemsInCategoryWithinTime(category, producentCodes, minListingDate, maxListingDate)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategoryWithinCurrentPrice(
			string category,
			string[] producentCodes,
			int? minPrice = null,
			int? maxPrice = null
			)
		{
			return _pcPartsRepo.GetItemsInCategoryWithinPrice(category, producentCodes, minPrice, maxPrice)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategory(string category, string[] producentCodes)
		{
			return _pcPartsRepo.GetItemsInCategory(category, producentCodes)
				.ToDictionary(g => g.Key, g => g.ToList());
		}
	}
}
using PcPartsScrap.Api.Data.Entities;
using System;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Api.Data.Repository.Interfaces
{
	public interface IPcPartsRepository
	{
		IEnumerable<string> GetCategories();

		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategory(string category, string[] producentCodes);

		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinPrice(string category, string[] producentCodes, int? minPrice = null, int? maxPrice = null, DateTime? tillDate = null, IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null);

		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTime(string category, string[] producentCodes, DateTime? minListingDate = null, DateTime? maxListingDate = null, IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null);

		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTimeAndPrice(string category, string[] producentCodes, DateTime? minListingDate = null, DateTime? maxListingDate = null, int? minPrice = null, int? maxPrice = null);

		Dictionary<string, string> GetItemsNamesInCategory(string category);
	}
}
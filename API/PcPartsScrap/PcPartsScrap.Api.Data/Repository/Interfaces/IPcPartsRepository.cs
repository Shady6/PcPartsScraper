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
		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinPrice(string category, SearchFilter filter, DateTime? tillDate = null, IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null);
		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTime(string category, SearchFilter filter, IEnumerable<IGrouping<string, PCParts>> itemsInCategory = null);
		IEnumerable<IGrouping<string, PCParts>> GetItemsInCategoryWithinTimeAndPrice(string category, SearchFilter filter);
		Dictionary<string, string> GetItemsNamesInCategory(string category);
	}
}
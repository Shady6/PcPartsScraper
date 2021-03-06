using PcPartsScrap.Api.Data;
using PcPartsScrap.Api.Data.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace PcPartsScrap.Api.Managers.Interfaces
{
	public interface IPcPartsManager
	{
		string[] GetCategories();
		Dictionary<string, string> GetItemsNamesInCategory(string category);
		Dictionary<string, List<PCParts>> SearchItemsWithFilter(string category, SearchFilter filter);
	}
}
using PcPartsScrap.Api.Managers.Interfaces;
using ServiceReference1;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PcPartsScrap.Api.Managers
{
	public class PcPartsManager : IPcPartsManager
	{
		public async static Task<List<string>> GetCategories()
		{
			PcPartsServiceClient service = new PcPartsServiceClient(PcPartsServiceClient.EndpointConfiguration.NetTcpBinding_IPcPartsService);
			var categories = new List<string>(await service.GetCategoriesAsync());
			return categories;
		}
	}
}
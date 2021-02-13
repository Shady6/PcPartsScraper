using PcPartsScrap.Wcf.Contracts;
using System.Collections.Generic;

namespace PcPartsScrap.Wcf.Services
{
	public class PcPartsService : IPcPartsService
	{
		public List<string> GetCategories()
		{
			return new List<string> { "GPU", "CPU" };
		}
	}
}
using System.Collections.Generic;
using System.ServiceModel;

namespace PcPartsScrap.Wcf.Contracts
{
	[ServiceContract]
	public interface IPcPartsService
	{
		[OperationContract]
		List<string> GetCategories();
	}
}
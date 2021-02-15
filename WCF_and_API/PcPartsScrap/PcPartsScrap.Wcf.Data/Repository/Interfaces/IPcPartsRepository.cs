using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PcPartsScrap.Wcf.Data.Repository.Interfaces
{
	public interface IPcPartsRepository
	{
		List<string> GetCategories();
	}
}

using PcPartsScrap.Wcf.Data.Repository.Interfaces;
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

		public List<string> GetCategories() => _dbContext.PcParts.GroupBy(p => p.Category)
				.Select(g => g.Key)
				.ToList();
	}
}
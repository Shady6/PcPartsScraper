using PcPartsScrap.Wcf.Data.Entities;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PcPartsScrap.Wcf.Data
{
	class PcPartsDbContext : DbContext
	{
		public PcPartsDbContext() : base("name=PCPartsDB")
		{

		}

		public DbSet<PcPart> PcParts { get; set; }
		public DbSet<ExchangeRate> ExchangeRates { get; set; }
	}
}

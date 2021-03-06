using Microsoft.EntityFrameworkCore;
using PcPartsScrap.Api.Data.Entities;

namespace PcPartsScrap.Api.Data
{
	public class PcPartsDbContext : DbContext
	{
		public PcPartsDbContext(DbContextOptions options) : base(options)
		{
		}

		public DbSet<PCParts> PcParts { get; set; }
		public DbSet<ExchangeRate> ExchangeRates { get; set; }
	}
}
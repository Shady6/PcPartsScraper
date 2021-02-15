using Autofac;
using PcPartsScrap.Wcf.Data;
using PcPartsScrap.Wcf.Data.Repository;
using PcPartsScrap.Wcf.Data.Repository.Interfaces;
using PcPartsScrap.Wcf.Services;

namespace PcPartsScrap.Wcf.Common.DI
{
	public static class Binder
	{
		public static IContainer Register()
		{
			var builder = new ContainerBuilder();

			builder.RegisterType<PcPartsDbContext>();
			builder.RegisterType<PcPartsRepository>().As<IPcPartsRepository>();
			builder.RegisterType<PcPartsService>();

			var container = builder.Build();
			return container;
		}
	}
}
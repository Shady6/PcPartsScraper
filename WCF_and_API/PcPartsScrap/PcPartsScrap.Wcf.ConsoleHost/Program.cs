using Autofac.Integration.Wcf;
using PcPartsScrap.Wcf.Common.DI;
using PcPartsScrap.Wcf.Services;
using System;
using System.Globalization;
using System.ServiceModel;
using System.Threading;

namespace PcPartsScrap.Wcf.ConsoleHost
{
	internal class Program
	{
		private static void Main(string[] args)
		{
			Thread.CurrentThread.CurrentUICulture = new CultureInfo("en-us");

			var container = Binder.Register();

			ServiceHost hostManager = new ServiceHost(typeof(PcPartsService));
			hostManager.AddDependencyInjectionBehavior(typeof(PcPartsService), container);

			hostManager.Open();

			Console.WriteLine("Service started. Press [enter] to exit.");
			Console.ReadLine();

			hostManager.Close();
		}
	}
}
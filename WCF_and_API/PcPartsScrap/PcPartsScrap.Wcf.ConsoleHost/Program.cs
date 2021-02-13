using PcPartsScrap.Wcf.Services;
using System;
using System.ServiceModel;

namespace PcPartsScrap.Wcf.ConsoleHost
{
	internal class Program
	{
		private static void Main(string[] args)
		{
			ServiceHost hostManager = new ServiceHost(typeof(PcPartsService));

			hostManager.Open();

			Console.WriteLine("Service started. Press [enter] to exit.");
			Console.ReadLine();

			hostManager.Close();
		}
	}
}
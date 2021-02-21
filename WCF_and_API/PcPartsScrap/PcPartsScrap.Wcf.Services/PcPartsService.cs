using PcPartsScrap.Wcf.Contracts;
using PcPartsScrap.Wcf.Data.Repository.Interfaces;
using System;
using System.Collections.Generic;

namespace PcPartsScrap.Wcf.Services
{
	public class PcPartsService : IPcPartsService
	{
		protected readonly IPcPartsRepository _pcPartsRepo;

		public PcPartsService(IPcPartsRepository pcPartsRepo)
		{
			_pcPartsRepo = pcPartsRepo;
		}

		public List<string> GetCategories()
		{
			throw new NotImplementedException();
			//return _pcPartsRepo.GetCategories();
		}
	}
}
using AutoMapper;
using PcPartsScrap.Api.Common.Extensions;
using PcPartsScrap.Api.Data;
using PcPartsScrap.Api.Data.DTOs;
using PcPartsScrap.Api.Data.Entities;
using PcPartsScrap.Api.Data.Repository.Interfaces;
using PcPartsScrap.Api.Managers.Interfaces;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Api.Managers
{
	public class PcPartsManager : IPcPartsManager
	{
		private readonly IPcPartsRepository _pcPartsRepo;
		private readonly IMapper _mapper;

		public PcPartsManager(IPcPartsRepository pcPartsRepo, IMapper mapper)
		{
			_pcPartsRepo = pcPartsRepo;
			_mapper = mapper;
		}

		public Dictionary<string, List<PcPartDto>> SearchItemsWithFilter(string category, SearchFilter filter)
		{
			Dictionary<string, List<PCParts>> result;

			switch (filter.FilterBy.ToEnum<FilterBy>())
			{
				case FilterBy.Price:
					result = GetItemsInCategoryWithinCurrentPrice(category, filter);
					break;
				case FilterBy.Date:
					result = GetItemsInCategoryWithinTime(category, filter);
					break;
				case FilterBy.PriceAndDate:
					result = GetItemsInCategoryWithinTimeAndPrice(category, filter);
					break;
				default:
					result = GetItemsInCategory(category, filter.ProducentCodes);
					break;
			}

			return _mapper.Map<Dictionary<string, List<PcPartDto>>>(result);
		}

		public string[] GetCategories()
		{
			return _pcPartsRepo.GetCategories().ToArray();
		}

		public Dictionary<string, string> GetItemsNamesInCategory(string category)
		{
			return _pcPartsRepo.GetItemsNamesInCategory(category);
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategoryWithinTimeAndPrice(string category, SearchFilter filter)
		{
			return _pcPartsRepo.GetItemsInCategoryWithinTimeAndPrice(category, filter)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategoryWithinTime(string category, SearchFilter filter)
		{
			return _pcPartsRepo.GetItemsInCategoryWithinTime(category, filter)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategoryWithinCurrentPrice(string category, SearchFilter filter)
		{
			return _pcPartsRepo.GetItemsInCategoryWithinPrice(category, filter)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		private Dictionary<string, List<PCParts>> GetItemsInCategory(string category, string[] producentCodes)
		{
			return _pcPartsRepo.GetItemsInCategory(category, producentCodes)
				.ToDictionary(g => g.Key, g => g.ToList());
		}

		Dictionary<string, List<PCParts>> IPcPartsManager.SearchItemsWithFilter(string category, SearchFilter filter)
		{
			throw new System.NotImplementedException();
		}
	}
}
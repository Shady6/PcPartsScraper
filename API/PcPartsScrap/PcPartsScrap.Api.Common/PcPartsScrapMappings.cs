using AutoMapper;
using PcPartsScrap.Api.Data.DTOs;
using PcPartsScrap.Api.Data.Entities;

namespace PcPartsScrap.Api.Common
{
	public class PcPartsScrapMappings : Profile
	{
		public PcPartsScrapMappings()
		{
			CreateMap<PCParts, PcPartDto>();
		}
	}
}
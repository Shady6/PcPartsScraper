using System;

namespace PcPartsScrap.Api.Data
{
	public class SearchFilter
	{
		public string[] producentCodes { get; set; }
		public string filterBy { get; set; }		
		public DateTime minListingDate { get; set; }
		public DateTime maxListingDate { get; set; }
		public int minPrice { get; set; }
		public int maxPrice { get; set; }		
	}
}
using System;

namespace PcPartsScrap.Api.Data
{
	public class SearchFilter
	{
		public string[] ProducentCodes { get; set; }
		public string FilterBy { get; set; }		
		public DateTime? MinListingDate { get; set; }
		public DateTime? MaxListingDate { get; set; }		
		public int? MinPrice { get; set; }
		public int? MaxPrice { get; set; }		
	}
}
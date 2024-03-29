﻿using System;

namespace PcPartsScrap.Api.Data.DTOs
{
	public class PcPartDto
	{		
		public string ShopName { get; set; }
		public string ProductName { get; set; }
		public string Category { get; set; }
		public string DetailedName { get; set; }
		public int Price { get; set; }
		public string ProducentCode { get; set; }
		public DateTime ListingDate { get; set; }
	}
}
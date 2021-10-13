using System;
using System.ComponentModel.DataAnnotations.Schema;
using System.Runtime.Serialization;

namespace PcPartsScrap.Api.Data.Entities
{
	[DataContract]
	public class PCParts
	{
		public int Id { get; set; }

		[Column(TypeName = "varchar")]
		public string ShopName { get; set; }

		[Column(TypeName = "varchar")]
		public string ProductName { get; set; }

		[Column(TypeName = "varchar")]
		public string Category { get; set; }

		public string DetailedName { get; set; }
		public int Price { get; set; }

		[Column(TypeName = "varchar")]
		public string ProducentCode { get; set; }

		public DateTime ListingDate { get; set; }
	}
}
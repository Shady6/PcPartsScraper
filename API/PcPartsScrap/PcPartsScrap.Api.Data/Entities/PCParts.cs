using System;
using System.ComponentModel.DataAnnotations.Schema;
using System.Runtime.Serialization;

namespace PcPartsScrap.Api.Data.Entities
{
	[DataContract]		
	public class PCParts
	{
		[DataMember]
		public int Id { get; set; }
		[DataMember]
		[Column(TypeName = "varchar")]
		public string ShopName { get; set; }
		[DataMember]
		[Column(TypeName = "varchar")]
		public string ProductName { get; set; }
		[DataMember]
		[Column(TypeName = "varchar")]		
		public string Category { get; set; }
		[DataMember]
		public string DetailedName { get; set; }
		[DataMember]
		public int Price { get; set; }
		[DataMember]
		[Column(TypeName = "varchar")]
		public string ProducentCode { get; set; }
		[DataMember]
		public DateTime ListingDate { get; set; }
	}
}
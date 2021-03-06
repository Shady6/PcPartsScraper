using System;
using System.Runtime.Serialization;

namespace PcPartsScrap.Api.Data.Entities
{
	[DataContract]
	public class ExchangeRate
	{
		[DataMember]
		public int Id { get; set; }
		[DataMember]
		public string FromTo { get; set; }
		[DataMember]
		public float Value { get; set; }
		[DataMember]
		public DateTime Date { get; set; }
	}
}
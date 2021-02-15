using System;

namespace PcPartsScrap.Wcf.Data.Entities
{
	public class ExchangeRate
	{
		public int Id { get; set; }
		public string FromTo { get; set; }
		public float Value { get; set; }
		public DateTime Date { get; set; }
	}
}
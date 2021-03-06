using PcPartsScrap.Api.Data.Attributes;

namespace PcPartsScrap.Api.Data
{
	public enum FilterBy
	{
		[StringValue("")]
		Nothing,
		[StringValue("P")]
		Price,
		[StringValue("D")]
		Date,
		[StringValue("PD")]
		PriceAndDate
	}
}

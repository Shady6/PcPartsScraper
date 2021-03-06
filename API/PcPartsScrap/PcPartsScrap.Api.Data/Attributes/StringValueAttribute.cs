using System;

namespace PcPartsScrap.Api.Data.Attributes
{
	[AttributeUsage(AttributeTargets.Field, AllowMultiple = false)]
	public class StringValueAttribute : Attribute
	{
		public readonly string StringValue;

		public StringValueAttribute(string stringValue)
		{
			this.StringValue = stringValue;
		}
	}
}
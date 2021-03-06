using PcPartsScrap.Api.Data.Attributes;
using System;
using System.Linq;
using System.Reflection;

namespace PcPartsScrap.Api.Common.Extensions
{
	public static class StringExtensions
	{
		public static T ToEnum<T>(this string str) where T : struct, IConvertible
		{
			if (!typeof(T).IsEnum)
			{
				throw new ArgumentException("T must be an enumerated type");
			}

			FieldInfo[] fieldInfos = typeof(T)
				.GetFields()
				.Where(m => m.DeclaringType == typeof(T) && m.Name != "value__")
				.ToArray();

			foreach (var field in fieldInfos)
			{
				StringValueAttribute attr = field.GetCustomAttribute<StringValueAttribute>(false);
				string value = "";

				if (attr != null && attr.StringValue == str || field.Name == str)
					return (T)field.GetValue(null);									
			}
			throw new ArgumentException("String didn't match with any of the enums");
		}
	}
}
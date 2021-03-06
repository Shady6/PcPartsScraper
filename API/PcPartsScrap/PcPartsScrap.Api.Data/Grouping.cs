using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Api.Data
{
	public class Grouping<TKey, TElement> : IGrouping<TKey, TElement>
	{
		public IEnumerable<TElement> Elements { get; set; }		
		public TKey Key { get; set; }

		public IEnumerator<TElement> GetEnumerator()
		{
			return this.Elements.GetEnumerator();
		}

		IEnumerator IEnumerable.GetEnumerator()
		{
			return GetEnumerator();
		}
	}
}
using Microsoft.AspNetCore.Mvc;
using PcPartsScrap.Api.Data;
using PcPartsScrap.Api.Data.Entities;
using PcPartsScrap.Api.Managers.Interfaces;
using System.Collections.Generic;
using System.Linq;

namespace PcPartsScrap.Api.Controllers
{
	[Route("api/[controller]")]
	[ApiController]
	public class PcPartsController : ControllerBase
	{
		private readonly IPcPartsManager _pcPartsManager;

		public PcPartsController(IPcPartsManager pcPartsManager)
		{
			_pcPartsManager = pcPartsManager;
		}

		[HttpGet]
		[Route("categories")]
		public ActionResult<string[]> Get()
		{
			var categories = _pcPartsManager.GetCategories();

			return Ok(categories);
		}

		[HttpGet]
		[Route("categories/{category}")]
		public ActionResult<Dictionary<string, List<PCParts>>> GetItemsInCategoryFiltered(string category, [FromBody] SearchFilter filter)
		{
			var itemsInCategory = _pcPartsManager.SearchItemsWithFilter(category, filter);

			return Ok(itemsInCategory);
		}

		[HttpGet]
		[Route("categories/{category}/names")]
		public ActionResult<Dictionary<string, string>> GetNamesInCategory(string category)
		{
			var namesInCategory = _pcPartsManager.GetItemsNamesInCategory(category);

			return Ok(namesInCategory);
		}
	}
}
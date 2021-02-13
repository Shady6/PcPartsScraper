using Microsoft.AspNetCore.Mvc;
using PcPartsScrap.Api.Managers;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PcPartsScrap.Api.Controllers
{
	[ApiController]
	[Route("[controller]")]
	public class WeatherForecastController : ControllerBase
	{
		public WeatherForecastController()
		{
		}

		[HttpGet]
		public async Task<ActionResult<List<string>>> Get()
		{
			var categories = await PcPartsManager.GetCategories();
			return Ok(categories);
		}
	}
}
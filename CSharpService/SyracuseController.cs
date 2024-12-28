
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

[ApiController]
[Route("api/syracuse")]
public class SyracuseController : ControllerBase
{
    [HttpPost]
    public IActionResult StoreResults([FromBody] SyracuseResult result)
    {
        // Simuler l'insertion dans une base de données ou un bucket
        Console.WriteLine(JsonSerializer.Serialize(result));
        return Ok(new { message = "Résultats stockés avec succès." });
    }
}

public class SyracuseResult
{
    public int Number { get; set; }
    public bool IsPair { get; set; }
    public int[] Sequence { get; set; }
}
        
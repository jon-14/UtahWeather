# Utah's Coldest Temperatures
<p><strong>Objective:</strong> Analyze current temperatures to identify the coldest temperature in Utah on a given day.</p>
<p><strong>Getting Started:</strong> Start simple by monitoring two locations: Kamas, UT and Brian Head, UT.</p>
<p>We will use Open Meteo's free web API (https://open-meteo.com), which is free up to 10,000 API calls per day.</p>
<p>API calls are of the form</p>
<p><em>https://api.open-meteo.com/v1/forecast?latitude=LatitudeCoordinate&longitude=LongitudeCoordinate&current=temperature_2m</em></p>

<p>Project Outline</p>
<p>Write Python code to do the following:</p>
<ol>
    <li>Contact Open Meteo API</li>
    <li>Store the data from the API in a database.</li>
</ol>
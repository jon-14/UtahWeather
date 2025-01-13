# Weather Data Analysis - Personal Project
<p><strong>Current objective:</strong>Collect and analyze data showing a correlation between change in temperature dtemp/dt (degrees Fahrenheit per hour) and elevation.</p>

<p>Data Sources</p>
<ul>
    <li>Open Meteo weather forecast API (https://open-meteo.com/en/docs)</li>
    <li>Open Meteo elevation API (https://open-meteo.com/en/docs/elevation-api)</li>
</ul>
<p>API calls are of the form https://api.open-meteo.com/v1/forecast?latitude=LatitudeCoordinate&longitude=LongitudeCoordinate&current=temperature_2m</p>

 <p>So far I have recorded data for five locations in Utah:</p>
        <ul>
            <li>Brian Head (elevation ~9835 ft)</li>
            <li>Kamas (elevation ~6,486 ft)</li>
            <li>Lucin (elevation ~4,465 ft)</li>
            <li>Mirror Lake (elevation ~10,056 ft)</li>
            <li>Salt Lake City (elevation ~ft)</li>
        </ul>

<p><em>Note:</em> This is a project in progress and will be updated periodically.</p>

## Current Findings
<p>Currently, the data I've collected suggests a link between elevation and change in temperature, but I would like to gather more information and have a more robust dataset.</p>
<ul>
   <li>Kamas and Mirror Lake have an overall higher rate of temperature change per hour than the other locations. Mirror Lake in particular seems to warm up more quickly in the 06:00 - 11:59 timeframe.</li>
   <li>I would like to collect data for more locations over a longer timeframe to better answer this question.</li>
   <li>I would also like to take into account the level of vegetation/forestation at the locations. For example, a forested area (e.g., Mirror Lake) might heat up/cool down less quickly than a similarly elevated location with no trees or vegetation.</li>
</ul>

### Average rate of change (degrees F per hour), broken out by time of day.
   <table>
        <th>
            <td>00:00 - 05:59</td>
            <td>06:00 - 11:59</td>
            <td>12:00 - 17:59</td>
            <td>18:00 - 23:59</td>
            <td>Overall</td>
            <td></td>        
        </th>
        <tr>
            <td>Brian Head</td>
            <td>-0.447</td>
            <td>1.625</td>
            <td>-0.339</td>
            <td>-0.626</td>
            <td>0.053</td>
        </tr>
        <tr>
            <td>Kamas</td>
            <td>-0.525</td>
            <td>1.634</td>
            <td>-0.015</td>
            <td>-0.701</td>
            <td>0.098</td>
        </tr>
        <tr>
            <td>Lucin</td>
            <td>-0.658</td>
            <td>1.535</td>
            <td>0.611</td>
            <td>-1.212</td>
            <td>0.069</td>
        </tr>        
        <tr>
            <td>Mirror Lake</td>
            <td>-0.842</td>
            <td>2.664</td>
            <td>-0.933</td>
            <td>-0.455</td>
            <td>0.109</td>
        </tr>        
        <tr>
            <td>Salt Lake City</td>
            <td>-0.309</td>
            <td>0.991</td>
            <td>-0.054</td>
            <td>-0.320</td>
            <td>0.077</td>
        </tr>  
    </table>
    <li>The next table shows the standard deviation of temperature for each location over the course of the data collection period. Standard deviation gives us intuition as to how "spread out" the data set is.</li>
    <br>
     <table>
        <th>
            <td>Standard Deviation of Temperature</td>        
        </th>
        <tr>
            <td>Brian Head</td>
            <td>8.422</td>
        </tr>
        <tr>
            <td>Kamas</td>
            <td>6.780</td>
        </tr>
        <tr>
            <td>Lucin</td>
            <td>6.057</td>
        </tr>        
        <tr>
            <td>Mirror Lake</td>
            <td>8.522</td>
        </tr>        
        <tr>
            <td>Salt Lake City</td>
            <td>4.931</td>
        </tr>  
    </table>
    </ul>
</ul>

## Repository Overview
<p>Python scripts</p>
<ul>
    <li>GetData</li>
    <ul>
        <li>get_weather_data: retrieves real time weather data from Open Meteo API.</li>
        <li>store_weather_data: stores data from API in a local databse.</li>
    </ul>
    <li>database_connection: a class to handle querying and inserting into a local mySql database.</li>
</ul>

<p>Next steps</p>
<ul>
    <li>Make more use of Python for analyzing data (either as a CSV or by storing the result set of queries in a dataframe).</li>
    <li>Refine store_weather_data to make use of the database_connection class.</li>
    <li>Add new locations</li>
    <li>Add a new column to track elevation.</li>
    <li>Another project idea -- try to find the coldest location in Utah at a given time. Use a random number generator to pick, say, 1000 latitude/longitude pairs within Utah and call the API for each pair.
</ul>

## Data Collected
<p>409 temperature recordings per location from 1/9/25 00:18 to 1/12/25 00:16. Average time between readings was about 10 minutes.</p>

<hr>
<br>
<p>Please feel free to reach out to me with any questions or comments about this project at coxjonathan2016@gmail.com</p>
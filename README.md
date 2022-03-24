# https---github.com-Vimanya-Saladstop
<h2>Data Preprocessing and Ingestion</h2>
<ul>
  <li>Explore the data and check for null values.replace '#SPILLS' in the amount column to NULL.</li>
  <li>Data In the excel file need to convert into csv or json to upload into mongodb.</li>
  <li>Pandas library for data preparation</li>
  <ul>
    <li>df = pd.read_csv('importdata.csv', parse_dates = ['Transaction date'])</li>
    <li>df = df.dropna(axis=0, subset=['Transaction date'])</li>
    <li>df = df.replace('#SPILL!', None)</li>
    <li>df.to_csv(r'saladstop.csv')</li>
    <li>df.to_json(r'saladstop.json',orient = 'records')</li>
  </ul>
  <li>In windows mongodb compass -</li>
   <ul>
     <li>Create Database - command prompt --> "mongo" command to open mongo shell --> "Use dbname" command to create database</li>
     <li>Connect the Localhost(http://127.0.0.1:27017/) server id, user name and password in mongodb compass UI.</li>
     <li>Select the database and Create Collection.</li>
     <li>Upload data into the database using "Add Data" button.</li>
  </ul>
  <li>In Linux mongodb -</li>
   <ul>
     <li>Create Database - command prompt --> "mongo" command to open mongo shell --> "Use dbname" command to create database.</li>
     <li>mongoimport --db mydb 
       --collection saladstop 
       --type csv 
       --columnsHaveTypes 
       --fields     Transaction_date.date,Supplier.string,Item_description.string,Country_of_origin.string,Quantity.int32,Unitprice_SGD.double,Price_Incl_Tax.double,Discount.double,Total.double,GST.double,Total_incl_GST.double 
       --file saladstop.csv
</li>
     <li></li>
  </ul>
</ul>
<h2>Django Dashboard Functions</h2>
<ul>
     <li>index function.</li>
      <ul>
        <li>Intially All the records in the database will Appear in the main html page.</li>
        <li>Two date pickers are available to select From date and To date</li>
        <li>After Selected the two dates , select the submit button. It will do Ajax call and transfer the signal(fromdate and todate) to "view.py".</li>
        <li>If "POST" request triggered , "if" statement will run and filter the data inbetween both selected dates(Through Queryset).</li>
        <li>Save the Queryset globally.</li>
        <li>Queryset return(through context) to html page and display the data.</li> 
      </ul>
     <li>Aggregation Function</li>
     <ul>
        <li>"Data Summary" button is there to load "summary_saladstop.html" page</li>
        <li>Queryset converted into pandas dataframe.</li>
        <li>Total Amount with GST = df['Total_incl_GST'].sum() </li>
        <li>Avg price per item without GST = groupby "Item_description" and get mean value of "Unitprice_SGD" for each item and sort by highest mean(sort()).This data displayed as a table</li>
       <li>Top Supplier Country = Tranfer string in 'Country_of_origin' to lowercase to avoid duplicates(str.lower()) and groupby 'Country_of_origin'. sum the quantity for each country(sum()). sort by descending to get top country on the top. </li>
      </ul>
  </ul>

<h2>Django Dashboard Runbook</h2>
<ul>
     <li>Run requirment.txt file to get libraries.</li>
     <li>Intialize the Database inside "setting.py".</li>
     <li>Run "python manage.py runserver" and direct to localhost:8000</li>
     <li> Find views.py and Test scripts inside the app_1 folder </li>
  </ul>

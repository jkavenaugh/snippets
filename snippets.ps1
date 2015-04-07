<#

	Some Powershell Snippets

#>

# MySQL connection

$mysql = New-Object MySql.Data.MySqlClient.MySqlConnection
$mysql.ConnectionString = "database=$database;server=$server;Persist Security Info=false;user id=$username;pwd=$password"

# Select some rows

$mysql.Open()
$command = New-Object MySQL.Data.MysqlClient.MySqlCommand
$command.Connection = $mysql
$command.CommandText = "SELECT * FROM table WHERE name LIKE '$Name'"

$reader = $command.ExecuteReader()

while($reader.Read()){ row = @{column1 = $reader.GetString(0)
                               column2 = $reader.GetString(1)
							   }
}

$reader.Close()
$mysql.Close()

# Perform an UPDATE

$command = New-Object MySQL.Data.MysqlClient.MySqlCommand
$command.Connection = $mysql
$command.CommandText = "UPDATE table SET name='$Name', email='$EmailAddress', company='$Department' WHERE id='$id'"

$result = $command.ExecuteNonQuery()

$mysql.Close()

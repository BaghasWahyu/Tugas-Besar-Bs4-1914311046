cd C:\Users\Baghas\Documents\MRIS\web_scraping\tugas2\wavfile

$list = Get-Content C:\Users\Baghas\Documents\MRIS\web_scraping\tugas2\link.txt

$clnt = New-Object System.Net.WebClient

foreach($url in $list) 
{ 

	#Get the filename 
	$filename = [System.IO.Path]::GetFileName($url) 

	#Create the output path 
	$file = [System.IO.Path]::Combine($pwd.Path, $filename) 

	Write-Host -NoNewline "Mengunduh ""$url""... "

	#Download the file using the WebClient 
	$clnt.DownloadFile($url, $file) 

	Write-Host "Selesai!." 
}
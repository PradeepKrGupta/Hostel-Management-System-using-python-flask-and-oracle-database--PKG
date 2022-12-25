<?php
    //set connection variables

    $server = "localhost";
    $username = "root";
    $password = "";
    $dbname = "htm";
    //create a database connection

    $con = mysqli_connect($server,$username,$password,$dbname);
    //To check connection built or not

   if(!$con){  

        die('Could not connect: '.mysqli_connect_error());  

    }  

    // echo 'Connected successfully<br/>';  

    $query1 = "SELECT * FROM `student`;";
    $connect1 = mysqli_query($con, $query1);

    $query2 = "SELECT `hid`, `name`, `bregno`, `gender`, `bname`, `floor`, `roomno` FROM `student`, `boyshostel`, `block` WHERE `student`.`regno`=`block`.`bregno` AND `boyshostel`.`branch`=`block`.`bname`;";
    $connect2 = mysqli_query($con, $query2);

    $query3 = "SELECT * FROM `boyshostel`;";
    $connect3 = mysqli_query($con, $query3);

    //check in database any data have or not
    
    $con->close();    
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Show data</title>
    <link rel="stylesheet" href="./css/style.css">
</head>

<body>
    <div class="mainContainer">
    
        <div class="showcontainer1">
            <h2 class="FirstContainerH2">Student Details</h2>
            <table border="1" cellspacing="0">
                <tr>
                    <th class="thead1">Regno</th>
                    <th class="thead1">Name</th>
                    <th class="thead1">Gender</th>
                    <th class="thead1">Date of Birth</th>
                    <th class="thead1">City</th>
                    <th class="thead1">State</th>
                    <th class="thead1">Country</th>
                </tr>

                <?php
                //check in database any data have or not
                if(mysqli_num_rows($connect1) > 0){
                    while($data=mysqli_fetch_assoc($connect1)){
                        echo "
                            <tr>
                                <td>".$data['regno']."</td>
                                <td>".$data['name']."</td>
                                <td>".$data['gender']."</td>
                                <td>".$data['dob']."</td>
                                <td>".$data['city']."</td>
                                <td>".$data['state']."</td>
                                <td>".$data['country']."</td>
                            </tr>
                        ";
                    }
                }
                
            ?>
            </table>

            <div class="showcontainer2">
                <h2>Your Hostel Details</h2>
                <table border="1" cellspacing="0">
                    <tr>
                        <th class="thead1">Block id</th>
                        <th class="thead1">Name</th>
                        <th class="thead1">Regno</th>
                        <th class="thead1">Gender</th>
                        <th class="thead1">Block name</th>
                        <th class="thead1">Floor</th>
                        <th class="thead1">Room no</th>
                    </tr>

                    <?php
                //check in database any data have or not
                if(mysqli_num_rows($connect2) > 0){
                    while($data=mysqli_fetch_assoc($connect2)){
                        echo "
                            <tr>
                                <td>".$data['hid']."</td>
                                <td>".$data['name']."</td>
                                <td>".$data['bregno']."</td>
                                <td>".$data['gender']."</td>
                                <td>".$data['bname']."</td>
                                <td>".$data['floor']."</td>
                                <td>".$data['roomno']."</td>
                            </tr>
                        ";
                    }
                }
                
            ?>
                </table>
            </div>

            <div class="showcontainer3">
                <h2>Hostel Details</h2>
                <table border="1" cellspacing="0">
                    <tr>
                        <th class="thead1">Hostel id</th>
                        <th class="thead1">regno</th>
                        <th class="thead1">Year</th>
                        <th class="thead1">Branch</th>
                    </tr>

                    <?php
                //check in database any data have or not
                if(mysqli_num_rows($connect3) > 0){
                    while($data=mysqli_fetch_assoc($connect3)){
                        echo "
                            <tr>
                                <td>".$data['hid']."</td>
                                <td>".$data['regno']."</td>
                                <td>".$data['year']."</td>
                                <td>".$data['branch']."</td>
                                
                            </tr>
                        ";
                    }
                }
                
            ?>
                </table>
            </div>
        </div>

        


</body>

</html>



<!-- ======================================================================
 -->

                    <td>{{item[1]}}</td>
                    <td>{{item[2]}}</td>
                    <td>{{item[3]}}</td>
                    <td>{{item[4]}}</td>
                    <td>{{item[5]}}</td>
                    <td>{{item[6]}}</td>
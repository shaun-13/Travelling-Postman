<?php

class UserDAO {
    
    public function retrieveAll() {
        $sql = 'SELECT * FROM user ORDER BY userid';
        
        $connMgr = new ConnectionManager();
        $conn = $connMgr->getConnection();
        
        $stmt = $conn->prepare($sql);
        $stmt->setFetchMode(PDO::FETCH_ASSOC);
        $stmt->execute();

        $arr = array();
        while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $user = new User($row['userid'],
                            $row['name'],
                            $row['travellerid'],
                            $row['requesterid'],
                            $row['password'],
                            $row['email']);
            $arr[] = $user; 
        }

        return $arr;
    }
    
    public function retrieve($email) {
        $sql = 'SELECT userid, name, travellerid, requesterid, password, email FROM user WHERE email=:email';
        
        $connMgr = new ConnectionManager();
        $conn = $connMgr->getConnection();
        
            
        $stmt = $conn->prepare($sql);
        $stmt->setFetchMode(PDO::FETCH_ASSOC);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->execute();

        while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            return new User($row['userid'],
                                $row['name'],
                                $row['travellerid'],
                                $row['requesterid'],
                                $row['password'],
                                $row['email']);
        }
    }

}
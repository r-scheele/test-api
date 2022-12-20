package httpapi.authz
import input
default allow = false




allow {
  some username  
  input.request_path = ["user", username] 
  input.preferred_username = username  
  
}



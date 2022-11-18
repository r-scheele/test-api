
package httpapi.authz
import input
default allow = false



# Allow access to a path, based on the path variable

allow {
  some username  
  input.request_path = ["user", username] 
  input.preferred_username = username  
  
}

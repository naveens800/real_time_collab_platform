import { gql } from '@apollo/client'

export const LOGIN_MUTATION = gql`
  mutation Login($username:String!, $password:String!){
    login(username:$username, password:$password){
      authPayload {
        user {
          id,
          username
        }
      }
    }
  }
`
export const GOOGLE_LOGIN = gql`
mutation GoogleLogin($token: String!) {
  googleLogin(token: $token) {
    user {
      id
      email
    }
  }
}
`
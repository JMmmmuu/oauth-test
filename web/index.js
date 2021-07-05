
const endpoint = "http://localhost:8000/graphql";

const query = `mutation verifyAuthCode ($verifyAuthCodeInput: VerifyAuthCodeInput) {
  verifyAuthCode (input: $verifyAuthCodeInput) {
    access
    refresh
  }
}`;

// const variables = {
//   "authCode": "",
//   "provider": "KAKAO"
// };

function success_login(variables) {
  console.log(variables);

  fetch(
    endpoint,
    {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({query: query, variables: {verifyAuthCodeInput: variables}}),
    }
  ).then(
    (res) => res.json()
  ).then(
    (result) => console.log(result)
  );
}

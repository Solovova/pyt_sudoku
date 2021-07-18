import com.fasterxml.jackson.databind.ObjectMapper
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import java.net.URL

class ClTest {
    fun get() {
        val client = OkHttpClient()
        val url = URL("http://127.0.0.1:5000/get")

        val request = Request.Builder()
            .url(url)
            .get()
            .build()

        val response = client.newCall(request).execute()

        val responseBody = response.body!!.string()

        //Response
        println("Response Body: " + responseBody)

        //we could use jackson if we got a JSON
        val mapperAll = ObjectMapper()
        val objData = mapperAll.readTree(responseBody)

        objData.get("data").forEachIndexed { index, jsonNode ->
            println("$index $jsonNode")
        }
    }

    fun post() {
        val client = OkHttpClient()
        val url = URL("http://127.0.0.1:5000/post")

        //just a string
        var jsonString = "{\"name\": \"Rolando\", \"job\": \"Fakeador\"}"

        //or using jackson
        val mapperAll = ObjectMapper()
        val jacksonObj = mapperAll.createObjectNode()
        jacksonObj.put("name", "Rolando")
        jacksonObj.put("job", "Fakeador")
        jacksonObj.put("a_key", "a_key_test")
        val jacksonString = jacksonObj.toString()

        val mediaType = "application/json; charset=utf-8".toMediaType()
        val body = jacksonString.toRequestBody(mediaType)

        val request = Request.Builder()
            .url(url)
            .post(body)
            .build()

        val response = client.newCall(request).execute()

        val responseBody = response.body!!.string()

        //Response
        println("Response Body: " + responseBody)

        //we could use jackson if we got a JSON
        val objData = mapperAll.readTree(responseBody)

        println("My name is " + objData.get("name").textValue() + ", and I'm a " + objData.get("job").textValue() + ".")
    }
}
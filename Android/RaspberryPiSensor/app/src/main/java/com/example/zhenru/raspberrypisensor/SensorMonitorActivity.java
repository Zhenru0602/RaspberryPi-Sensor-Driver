package com.example.zhenru.raspberrypisensor;

import android.content.Intent;
import android.os.Handler;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class SensorMonitorActivity extends AppCompatActivity {
    String ip = "";
    Thread serverThread;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sensor_monitor_actvity);

        Bundle extras = getIntent().getExtras();
        ip = extras.getString("IP");

        serverThread = new Thread(new MyServerThread());
        serverThread.start();
    }

    @Override
    public void onDestroy() {
        serverThread.interrupt();
        super.onDestroy();
    }

    class MyServerThread implements Runnable{
        //create socket for connection
        Socket socket = null;
        InputStream in;
        Handler handler = new Handler();
        String message;
        String temperature, humidity, smoke, motion;

        @Override
        public void run(){
            try{
                socket = new Socket(ip, 6666);
                in = socket.getInputStream();
                byte[] buffer = new byte[1024];
                int bytes;
                boolean connection = true;
                while(connection){
                    bytes = in.read(buffer);
                    if(bytes != -1){
                        message = new String(buffer, "UTF-8");
                        try {
                            JSONObject sensorJson = new JSONObject(message);
                            temperature = sensorJson.getString("temperature");
                            humidity = sensorJson.getString("humidity");
                            smoke = sensorJson.getString("smoke");
                            motion = sensorJson.getString("motion");
                            Log.v("SensorMessage", message);
                            Log.v("SensorInfo",temperature+" "+humidity+" "+smoke+" "+motion);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                        handler.post(new Runnable() {
                            @Override
                            public void run() {
                                TextView text = findViewById(R.id.Temperature);
                                text.setText("temperature:" + temperature);
                                text = findViewById(R.id.Humidity);
                                text.setText("humidity: " + humidity);
                                text = findViewById(R.id.Smoke);
                                text.setText("smoke: " + smoke);
                                text = findViewById(R.id.Motion);
                                text.setText("motion: " + motion);
                            }
                        });
                    }
                    else{
                        socket.close();
                        connection = false;
                        Intent intent = new Intent(SensorMonitorActivity.this, FailActivity.class);
                        startActivity(intent);
                        finish();
                    }
                    buffer = new byte[1024];
                }
            } catch(IOException e){
                e.printStackTrace();
                Intent intent = new Intent(SensorMonitorActivity.this, FailActivity.class);
                startActivity(intent);
                finish();
            }
        }

    }
}

package com.example.zhenru.raspberrypisensor;

import android.content.Intent;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    void onClick(View v){
        EditText ipInputView = findViewById(R.id.ip_input);
        String ipInput = ipInputView.getText().toString();

        Intent intent = new Intent(MainActivity.this, SensorMonitorActivity.class);
        intent.putExtra("IP", ipInput);
        startActivity(intent);
        finish();
    }
}

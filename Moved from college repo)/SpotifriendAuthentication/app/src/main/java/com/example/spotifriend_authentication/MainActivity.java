package com.example.spotifriend_authentication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements View.OnClickListener
{
    private TextView txt_reg;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txt_reg = (TextView) findViewById(R.id.txt_reg);
        txt_reg.setOnClickListener(this);
    }

    @Override
    public void onClick(View view)
    {

    }
}
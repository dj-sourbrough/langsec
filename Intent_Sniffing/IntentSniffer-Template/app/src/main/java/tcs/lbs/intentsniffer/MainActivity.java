package tcs.lbs.intentsniffer;

import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.os.Bundle;
import android.widget.TextView;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.location.Location;

public class MainActivity extends AppCompatActivity
{
    static final String WEATHER_RECEIVER = "tcs.lbs.weather_app.WeatherBroadcastReceiver";
    static final String LOCATION_RECEIVER = "tcs.lbs.locationapp.MainActivityReceiver";
    TextView LatitudeTextView, LongitudeTextView;
    SnifferBroadcastReceiver wReceiver ;
    SnifferBroadcastReceiver lReceiver ;
    Location location;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LatitudeTextView = findViewById(R.id.LatitudeTextView);
        LongitudeTextView = findViewById(R.id.LongitudeTextView);

        /*
        IntentFilter wFilter = new IntentFilter();
        wFilter.addAction(WEATHER_RECEIVER);
        wReceiver = new SnifferBroadcastReceiver();
        registerReceiver(wReceiver, wFilter, Manifest.permission.ACCESS_FINE_LOCATION, null);
         */

        IntentFilter lFilter = new IntentFilter();
        lFilter.addAction(LOCATION_RECEIVER);
        lReceiver = new SnifferBroadcastReceiver();
        registerReceiver(lReceiver, lFilter);
    }
    protected class SnifferBroadcastReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            location = intent.getParcelableExtra("Location");
            if (location!=null) {
                double latitude = location.getLatitude();
                double longitude = location.getLongitude();

                LatitudeTextView.setText(String.valueOf(latitude));
                LongitudeTextView.setText(String.valueOf(longitude));
            }

            }
    }
}
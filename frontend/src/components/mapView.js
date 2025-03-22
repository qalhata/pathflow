// src/components/MapView.js
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const MapView = () => (
  <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '100vh' }}>
    <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
    <Marker position={[51.505, -0.09]}>
      <Popup>Pothole Location</Popup>
    </Marker>
  </MapContainer>
);

export default MapView;

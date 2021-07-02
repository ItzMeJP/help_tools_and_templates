## Eigen Tips


To convert quaternions to Euler angles (not cumulative) considering ZYZ order:


```
result = quaternion_orientation_.matrix().eulerAngles(2,1,2); //ZYZ
```

or ZXZ order, and so on...

```
result = quaternion_orientation_.matrix().eulerAngles(2,0,2); //ZXZ
```


To convert quaternions to Tait-Brian angles (Euller cumulative) and considering ZYX order:

```
/// <summary>
/// Transform a quaternion angle representation to Tait-Bryan (or cumulative Euler) angle. The construction sequence is ZYX
/// </summary>
/// <param name="_q"> Quaternion.</param>
/// <returns> The Vector3 with Roll(x), Pitch(y) and Yaw(z) angles.</returns>
Eigen::Vector3d Pose::getTaitBryanZYXFromQuaternion(Eigen::Quaterniond _q) {
    //https://marc-b-reynolds.github.io/math/2017/04/18/TaitEuler.html

    double x = _q.x(),
            y = _q.y(),
            z = _q.z(),
            w = _q.w();

    Eigen::Vector3d output;

    double t0 = x * x - z * z,
           t1 = w * w - y * y,
           xx = 0.5 * (t0 + t1),            // 1/2 x of x'
           xy = x * y + w * z,              // 1/2 y of x'
           xz = w * y - x * z,              // 1/2 z of x'
           t = xx * xx + xy * xy,           // cos(theta)^2
           yz = 2.0 * (y * z + w * x);      // z of y'

    output.z() = (float) atan2(xy, xx);         // yaw   (psi)
    output.y() = (float) atan(xz / sqrt(t)); // pitch (theta)

    if (t != 0)
        output.x() = (float) atan2(yz, t1 - t0);
    else
        output.x() = (float) (2.0 * atan2(x, w) - sgnd(xz) * output.z());

    return output;
}

double Pose::sgnd(double _in) {
    return (_in > 0.0) ? 1.0 : ((_in < 0.0) ? -1.0 : 0.0);
}
```

To get quaternion based on Euller representation (it works with cumulative or not...):
```
quaternion_orientation_ = Eigen::AngleAxisd(rpy_zyx_orientation_.z(), Eigen::Vector3d::UnitZ())
                          * Eigen::AngleAxisd(rpy_zyx_orientation_.y(), Eigen::Vector3d::UnitY())
                          * Eigen::AngleAxisd(rpy_zyx_orientation_.x(), Eigen::Vector3d::UnitX());
```                          

# ROS transformation tips.



- Nomenclatura do ROS:
frame de interesse (source_frame) em relação a uma base (target_frame).

- Exemplo do tf_echo

rosrun tf_echo interesse em_relacao_a_base

- As posições e TF tem a seguinte ordem (o valor que se insere nos campos de orientation  translation):
transladar -> rotacionar

- Para rotacionar, o ROS utiliza a ordem ZYX acumulativo

#### REF
http://wiki.ros.org/geometry/CoordinateFrameConventions

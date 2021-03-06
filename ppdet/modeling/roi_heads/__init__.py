# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from . import bbox_head
from . import mask_head
from . import cascade_head
from . import htc_bbox_head
from . import htc_mask_head
from . import htc_semantic_head

from .bbox_head import *
from .mask_head import *
from .cascade_head import *
from .htc_bbox_head import *
from .htc_mask_head import *
from .htc_semantic_head import *
